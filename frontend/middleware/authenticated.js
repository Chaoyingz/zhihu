import axios from 'axios'

export default function ({ isServer, req }) {
    if (isServer) {
        const token = localStorage.getItem('token')
        axios.defaults.headers.common['Authorization'] = `JWT ${token}`
    }
}
