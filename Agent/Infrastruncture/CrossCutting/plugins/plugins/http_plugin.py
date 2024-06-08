from pluggy import HookimplMarker
import requests
import json as json_lib

hookimpl = HookimplMarker("http")

@hookimpl
async def call_api(job_data):
    try:
        method = job_data['method'].lower()
        url = job_data['url']
        headers = job_data.get('headers', {})
        params = job_data.get('params', {})
        data = job_data.get('data', {})
        json = job_data.get('json', {})
        auth = job_data.get('auth', None)
        timeout = job_data.get('timeout', 10)  # Timeout padrão de 10 segundos
        hooks = job_data.get('hooks', {})

        response = None

        if method == 'get':
            response = requests.get(url, headers=headers, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'post':
            response = requests.post(url, headers=headers, data=data, json=json, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'put':
            response = requests.put(url, headers=headers, data=data, json=json, params=params, auth=auth, timeout=timeout, hooks=hooks)
        elif method == 'delete':
            response = requests.delete(url, headers=headers, params=params, auth=auth, timeout=timeout, hooks=hooks)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        
        if response.headers.get('Content-Type') == 'application/json':
                response_json = response.json()
        else:
            # Tentar converter manualmente para JSON
            try:
                response_json = json_lib.loads(response.text)
            except json_lib.JSONDecodeError:
                response_json = response.text

        return {
            'status_code': response.status_code,
            'headers': dict(response.headers),
            'content': response_json,
            'json': response.json() if response.headers.get('Content-Type') == 'application/json' else None
        }
    except Exception as ex:
        raise Exception(str(ex))
