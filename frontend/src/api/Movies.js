import axios from 'axios'

const api = axios.create({
    baseURL: 'https://api.themoviedb.org/3/',
    headers: {
        Authorization: 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkZTAwYzkwMzg5ZDdkMzQ1ZmJjYTA0NTBmYTIwM2YzMyIsInN1YiI6IjY1MDQ2ODNhNjNhYWQyMDBlMTJkMzc1ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Fa2Am6QtHiqSG7gWSb2O_8zykHjiFZHkYvWnbrrw1sg'
    }
})

export default api