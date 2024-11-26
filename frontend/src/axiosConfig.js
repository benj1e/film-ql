import axios from "axios";
const axiosInstance = axios.create({
    baseURL: "/api",
});

// Add a response interceptor
axiosInstance.interceptors.response.use(
    (response) => response,
    (error) => Promise.reject(error)
);

export default axiosInstance;
