import { boot } from "quasar/wrappers";
import axios from "axios";
import { LocalStorage } from "quasar";

// Определяем базовый URL для API в зависимости от среды
const domain = process.env.DEV
  ? "http://127.0.0.1:8000"
  : "http://dreammanor.ru";

// Устанавливаем стандартные заголовки
const headers = {
  Accept: "application/json",
};

// Создаём экземпляр axios с базовыми настройками
const api = axios.create({
  baseURL: domain + "/api/v1/",
  withCredentials: true,
  headers: headers,
});

// Функция для установки токена глобально
function setAuthorizationHeader(token) {
  api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
}

// Boot файл
export default boot(({ app }) => {
  // Получаем токен из LocalStorage и добавляем его в заголовки, если он существует
  const token = LocalStorage.getItem("token");
  if (token) {
    setAuthorizationHeader(token); // Устанавливаем токен при загрузке
  }

  // Глобальное использование axios в Vue компонентах
  app.config.globalProperties.$axios = axios;
  app.config.globalProperties.$api = api;
});

// Экспортируем функцию для динамического добавления токена
export { api, setAuthorizationHeader };
