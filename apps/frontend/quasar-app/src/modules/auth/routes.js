export default [
  {
    path: "/login",
    component: () => import("./layouts/MainLayout.vue"),
    children: [
      {
        path: "",
        name: "login",
        component: () => import("./pages/LoginPage.vue"),
      },
    ],
  },
  {
    path: "/forgot-password",
    component: () => import("./layouts/MainLayout.vue"),
    children: [
      {
        name: "passwordReset",
        path: "",
        component: () => import("./pages/ResetPage.vue"),
      },
    ],
  },
  {
    path: "/registration",
    component: () => import("./layouts/MainLayout.vue"),
    children: [
      {
        name: "registration",
        path: "",
        component: () => import("./pages/RegistrationPage.vue"),
      },
    ],
  },
  {
    path: "/logout",
    component: () => import("./layouts/MainLayout.vue"),
    children: [
      {
        name: "logout",
        path: "",
        meta: { auth: true }, // Доступ только для авторизованных пользователей
        component: () => import("./pages/LogoutPage.vue"),
      },
    ],
  },
  /**
  {
    path: "/users",
    component: () => import("./layouts/MainLayout.vue"),
    meta: { auth: true, superuser: true }, // Доступ только для суперпользователей
    children: [
      {
        name: "usersList",
        path: "",
        component: () => import("./pages/UsersList.vue"),
      },
    ],
  },
   */
];
