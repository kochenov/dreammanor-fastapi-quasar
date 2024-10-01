import { api } from "boot/axios";

/*
 * Добавьте перехватчик ответов
 */
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && [401, 419].includes(error.response.status)) {
      console.info(
        "[401, 419]: Пользователь не авторизован, не удалось войти в систему с помощью API"
      );
    }
    return Promise.reject(error);
  }
);

export default {
 /**
   * Сервис входа на сайт
   * @param {*} payload
   * @returns
   */
 async login(payload) {
  // Преобразуем payload в URL-кодированную строку
  const formData = new URLSearchParams();
  formData.append("username", payload.username);
  formData.append("password", payload.password);

  return await api.post("/auth-service/login", formData, {
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
},
  async logout() {
    return await api.post("/auth-service/logout");
  },
  async forgotPassword(payload) {
    await api.get("/sanctum/csrf-cookie");
    return api.post("/forgot-password", payload);
  },
  // Получает текущего пользователя
  async getAuthUser() {
    let result = await api.get("/auth-service/user/me");
    return result.data;
  },
  async resetPassword(email) {
    return await sendPasswordResetEmail(auth, email);
  },
  async registerUser(payload) {
    return await api.post("/auth/register", payload);
  },
  sendVerification(payload) {
    return api.post("/email/verification-notification", payload);
  },
};
