import { defineStore } from "pinia";
import { api, setAuthorizationHeader } from "boot/axios"; // Импортируем обновление токена
import AuthService from "./authService";
import { LocalStorage, Notify } from "quasar";
import { useRouter } from "vue-router";


export const useAuthStore = defineStore("authStore", {
  state: () => ({
    user: null, // Текущий пользователь
    currentRoute: null, // Маршрут, на который нужно вернуться после входа
    error: null, // Для хранения ошибки
    loading: false, // Флаг загрузки
  }),

  actions: {
    async login(payload, router) { // Передаем router как аргумент
      try {
        const { data, status } = await AuthService.login(payload);

        if (status === 200 && data?.access_token) {
          LocalStorage.set("token", data.access_token);
          Notify.create({ message: "Выполнен успешный вход!", color: "green" });

          // Устанавливаем токен в заголовки API запросов глобально
          setAuthorizationHeader(data.access_token);

          // Небольшая задержка перед запросом, чтобы гарантировать передачу токена
          setTimeout(async () => {
            await this.getAuthUser();  // Обновляем состояние пользователя сразу после входа

            const redirectPath = this.currentRoute || "/";
            router.push(redirectPath);  // Используем переданный router
            this.currentRoute = null; // Сбрасываем сохранённый маршрут
          }, 100);  // 100 мс задержки
        }
      } catch (error) {
        this.handleError(error);
      }
    },

    // Метод для выхода пользователя
    async logout() {
      try {
        const res = await AuthService.logout();
        if (res.status === 204) {
          this.user = null;
          LocalStorage.remove("token"); // Удаляем токен из хранилища
          this.router.push("/login"); // Перенаправляем на страницу входа
        }
      } catch (error) {
        this.user = null;
        console.log(error);
      }
    },

    // Получение текущего пользователя
    async getAuthUser() {
      try {
        this.loading = true;
        this.user = await AuthService.getAuthUser();
        this.loading = false;
      } catch (error) {
        this.user = null;
        this.loading = false;
        this.error = error;
      }
    },

    // Метод для регистрации пользователя
    async registration(payload) {
      try {
        const userCreditals = await AuthService.registerUser(payload);
        Notify.create({
          message: "Вы успешно зарегистрировались! Теперь можно войти на сайт",
          color: "green",
        });
        this.router.push({ path: "/login" });
      } catch (error) {
        if (error.response.data.detail === "REGISTER_USER_ALREADY_EXISTS") {
          Notify.create({
            message: "Пользователь с такими данными уже зарегистрирован",
            color: "red",
          });
        }
      }
    },

    // Сброс пароля
    async resetPassword(email) {
      try {
        await AuthService.resetPassword(email);
        Notify.create({
          message: "Для восстановления аккаунта проверьте ваш почтовый ящик",
        });
      } catch (error) {
        Notify.create({ message: error.code });
      }
    },

    handleError(error) {
      this.error = error;
      Notify.create({ message: error.message || "Ошибка!" });
    },
  },

  getters: {
    loggedIn: (state) => !!state.user, // Проверка, авторизован ли пользователь
    isAdmin: (state) => state.user && state.user.isAdmin, // Проверка, является ли пользователь админом
  },
});
