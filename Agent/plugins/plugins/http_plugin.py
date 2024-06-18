from pluggy import HookimplMarker
import requests
import json as json_lib

hookimpl = HookimplMarker("http")

@hookimpl
async def call_api(job_data):
    try:
        # Extrair informações do job_data
        method = job_data['method'].lower()
        url = job_data['url']
        headers = job_data.get('headers', {})
        params = job_data.get('params', {})
        data = job_data.get('data', {})
        json = job_data.get('json', {})
        auth = job_data.get('auth', None)
        timeout = job_data.get('timeout', 10)  # Timeout padrão de 10 segundos
        hooks = job_data.get('hooks', {})
        
        # Script de autenticação (opcional)
        auth_script = job_data.get('auth_script', None)

        # Executar script de autenticação, se houver
        if auth_script:
            local_vars = {}
            exec(auth_script, {}, local_vars)
            # Atualizar headers ou outras informações com os resultados do script
            headers.update(local_vars.get('headers', {}))
            params.update(local_vars.get('params', {}))
            data.update(local_vars.get('data', {}))
            json.update(local_vars.get('json', {}))
            if 'auth' in local_vars:
                auth = local_vars['auth']

        # Realizar a chamada HTTP
        response = None
        if method == 'get':
            response = requests.get(url, headers=headers, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'post':
            response = requests.post(url, headers=headers, data=data, json=json, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'put':
            response = requests.put(url, headers=headers, data=data, json=json, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'delete':
            response = requests.delete(url, headers=headers, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'patch':
            response = requests.patch(url, headers=headers, data=data, json=json, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'head':
            response = requests.head(url, headers=headers, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'options':
            response = requests.options(url, headers=headers, params=params, auth=auth, timeout=timeout, hooks=hooks)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        # Try to parse the response as JSON
        response_content = response.text
        try:
            response_json = response.json()
        except json_lib.JSONDecodeError:
            response_json = None

        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response_content,
            'json': response_json
        }
    except Exception as ex:
        raise Exception(str(ex))
