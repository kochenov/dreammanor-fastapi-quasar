export default [
  {
    path: "parsing/list",
    name: "ParsingLinks",
    meta: { auth: true,  superuser: true, title: "Список объявлений" },
    component: () => import("./pages/ParsingListPage.vue"),
    props: (route) => ({ page: Number(route.query.page) || 1 })
  },
  {
    path: "/announcement/new",
    name: "create-new-announcement",
    meta: { auth: true, title: "Новое объявление" },
    component: () => import("./pages/NewAnnouncementPage.vue"),
  },
];
