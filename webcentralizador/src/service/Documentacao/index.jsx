import { data } from "autoprefixer";
import { URL_CENTRALIZADOR } from "../../constants/webconst";
import axios from 'axios';

const url = URL_CENTRALIZADOR +'/Documentacao/api/'


export const getDocumentacao = async () => {
    try {
        const response = await axios.get(url + 'documentacao');
        if (response.status === 200) {
            return response.data;
           
        } else {
            return 'Erro ao servidores!';
        }
    } catch (error) {
        if (error.response && error.response.status === 404) {
            return error.response.data.mensagem;
        } else {
            return 'Erro de rede!';
        }
    }
}

export const getDocumentacao_chave = async (nmChavePlugin) => {
    try {
        const response = await axios.get(url + 'documentacao/' + nmChavePlugin);
        if (response.status === 200) {
            return response.data;
           
        } else {
            return 'Erro ao servidores!';
        }
    } catch (error) {
        if (error.response && error.response.status === 404) {
            return error.response.data.mensagem;
        } else {
            return 'Erro de rede!';
        }
    }
}

export const postDocumentacao = async (flAtivo) => {
    try {
        const response = await axios.post(url + 'documentacao/' + flAtivo);
        if (response.status === 200) {
            return response.data;
           
        } else {
            return 'Erro ao servidores!';
        }
    } catch (error) {
        if (error.response && error.response.status === 404) {
            return error.response.data.mensagem;
        } else {
            return 'Erro de rede!';
        }
    }
}

export const patchDocumentacao = async (Descricao) => {
    try {
        const response = await axios.patch(url + 'documentacao');
        if (response.status === 200) {
            return response.data;
           
        } else {
            return 'Erro ao servidores!';
        }
    } catch (error) {
        if (error.response && error.response.status === 404) {
            return error.response.data.mensagem;
        } else {
            return 'Erro de rede!';
        }
    }
}

export const deleteDocumentacao = async (nrDescricaoId) => {
    try {
        const response = await axios.delete(url + 'documentacao/' +nrDescricaoId );
        if (response.status === 200) {
            return response.data;
           
        } else {
            return 'Erro ao servidores!';
        }
    } catch (error) {
        if (error.response && error.response.status === 404) {
            return error.response.data.mensagem;
        } else {
            return 'Erro de rede!';
        }
    }
}