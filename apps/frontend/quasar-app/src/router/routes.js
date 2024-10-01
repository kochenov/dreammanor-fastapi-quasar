import { routes as authRoutes } from "src/modules/auth";
import { routes as realEstateRoutes } from "src/modules/real_estate";


const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/', component: () => import('pages/IndexPage.vue') }
    ]
  },
  {
    path: "/real-estate",
    name: "desk",
    meta: {},
    component: () => import("layouts/MainLayout.vue"),
    children: [...realEstateRoutes],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default [...routes, ...authRoutes];
