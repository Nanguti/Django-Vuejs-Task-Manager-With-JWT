import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import CreateTask from "../views/CreateTask.vue";
import TaskDetail from "../views/TaskDetail.vue";
import UpdateTask from "../views/UpdateTask.vue";
const routes = [
  {
    meta: {
      title: "Dashboard",
      requiresAuth: true,
    },
    path: "/",
    name: "dashboard",
    component: Dashboard,
  },
  {
    meta: {
      title: "Create Task",
      requiresAuth: true,
    },
    path: "/create-task",
    name: "create-task",
    component: CreateTask,
  },

  {
    meta: {
      title: "Task Detail",
      requiresAuth: true,
    },
    path: "/tasks/:taskId/",
    name: "task-detail",
    component: TaskDetail,
  },
  {
    meta: {
      title: "Update Task",
      requiresAuth: true,
    },
    path: "/update-task/:taskId",
    name: "update-task",
    component: UpdateTask,
  },
  {
    meta: {
      title: "Login",
    },
    path: "/login",
    name: "/login",
    component: Login,
  },
  {
    meta: {
      title: "Register",
    },
    path: "/register",
    name: "/register",
    component: Register,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const accessToken = localStorage.getItem("accessToken");
  if (to.meta.requiresAuth && !accessToken) {
    next("/login");
  } else {
    next();
  }
});

export default router;
