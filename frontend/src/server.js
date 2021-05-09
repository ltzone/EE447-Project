import axios from 'axios'
import vm from './main.js'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'

const errorComposer = (error) => {
    return (msg, url) => {
        // const status = error.response ? error.response.status : null
        if (error.response) {
            // Request made and server responded out of range of 2xx codes
            console.log(error.response)
            let data = JSON.stringify(error.response.data)
            if (data.length > 400) {
                data = data.slice(0, 400)
            }

            vm.$toasted.global.alert_error_detailed({
                header: `${msg}<br>\n
                           Please copy error data to clipboard and send it to admins<br>\n`,
                message: `${error}<br>URL: ${instance.defaults.baseURL}/${url}<br>${data}`,
            })
        } else if (error.request) {
            // The request was made but no response was received
            console.log('No response, request:', error.request)
            vm.$toasted.global.alert_error(`${error}<br> URL: ${instance.defaults.baseURL}/${url}`)
        } else {
            console.log('Something happened in setting up the request that triggered an Error:', error.message)
            vm.$toasted.global.alert_error(`${error}<br> URL: ${instance.defaults.baseURL}/${url}`)
        }
    }
}

const instance = axios.create({
    baseURL: '/api',
    // process.env.NODE_ENV !== 'production' ?
    //     process.env.VUE_APP_API_BASE_URL + ':' + process.env.VUE_APP_API_PORT :
    //         process.env.VUE_APP_API_BASE_URL
})

instance.interceptors.response.use(undefined, function (error) {
    error.handleGlobally = errorComposer(error)
    return Promise.reject(new Error(...error))
})

export default instance
