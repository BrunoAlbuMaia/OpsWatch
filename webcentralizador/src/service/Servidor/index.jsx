import { URL_CENTRALIZADOR } from "../../constants/webconst";
import axios from 'axios';

const url = URL_CENTRALIZADOR +'/Servidores/api/'


export const getServidoresAll = async () => {
    try {
        const response = await axios.get(url + 'servidor');
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

export const getServidores = async (flAtivo) => {
    try {
        const response = await axios.get(url + 'servidor/' + flAtivo);
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