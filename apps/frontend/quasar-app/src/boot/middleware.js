import { boot } from "quasar/wrappers";
import { useAuthStore } from "stores/all"; // Подключаем store для работы с авторизацией
import { LocalStorage } from "quasar"; // Для работы с локальным хранилищем

export default boot(async ({ router }) => {
  // Определяем маршруты, которые доступны только для гостей
  const guestAuthRoutes = ["login", "registration", "forgotPassword", "passwordReset"];

  router.beforeEach(async (to, from) => {
    const authStore = useAuthStore(); // Получаем состояние авторизации из store

    // Проверяем наличие токена в LocalStorage и получаем текущего пользователя
    const token = LocalStorage.getItem("token");
    if (token) {
      await authStore.getAuthUser(); // Получаем данные текущего пользователя
    }

    // Сохраняем текущий маршрут для дальнейшего редиректа после входа
    if (to.meta.auth && !authStore.user) {
      authStore.currentRoute = to.fullPath; // Сохраняем путь в состоянии
      return {
        path: "/login", // Переадресуем на страницу логина
        query: { redirect: to.fullPath }, // Сохраняем redirect в параметрах запроса
      };
    }

    // Проверка доступа только для суперпользователей
    if (to.meta.superuser && (!authStore.user || !authStore.user.is_superuser)) {
      return { path: "/" }; // Переадресация на главную страницу, если пользователь не суперпользователь
    }


    // Переадресуем авторизованного пользователя, если он пытается зайти на страницу для гостей
    if (authStore.user && guestAuthRoutes.includes(to.name)) {
      return { path: "/login" }; // Переадресуем на главную страницу, если авторизован
    }

  });
});
