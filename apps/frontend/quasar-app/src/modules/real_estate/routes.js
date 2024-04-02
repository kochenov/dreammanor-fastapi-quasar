export default [
  {
    path: "parsing/list",
    name: "ParsingLinks",
    meta: { auth: true, title: "Список объявлений" },
    component: () => import("./pages/ParsingListPage.vue"),
  },
  {
    path: "/announcement/new",
    name: "create-new-announcement",
    meta: { auth: true, title: "Новое объявление" },
    component: () => import("./pages/NewAnnouncementPage.vue"),
  },
];
