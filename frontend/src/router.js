import { createRouter, createWebHistory } from "vue-router";
import HomePage from "@/views/HomePage.vue";
import QuizDetail from "@/views/QuizDetail.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/quiz/:id",
    name: "QuizDetail",
    component: QuizDetail,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
