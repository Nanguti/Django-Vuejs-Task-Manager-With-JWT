import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "../views/Dashboard.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import CreateTask from "../views/tasks/CreateTask.vue";
import TaskDetail from "../views/tasks/TaskDetail.vue";
import UpdateTask from "../views/tasks/UpdateTask.vue";
import Users from "../views/users/Users.vue";
import Categories from "../views/categories/Categories.vue";
import CreateCategory from "../views/categories/CreateCategory.vue";
import UpdateCategory from "../views/categories/UpdateCategory.vue";

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
      title: "Users List",
      requiresAuth: true,
    },
    path: "/users/",
    name: "users",
    component: Users,
  },

  {
    meta: {
      title: "Categories List",
      requiresAuth: true,
    },
    path: "/categories/",
    name: "categories",
    component: Categories,
  },

  {
    meta: {
      title: "Create Category",
      requiresAuth: true,
    },
    path: "/create-category",
    name: "create-category",
    component: CreateCategory,
  },

  {
    meta: {
      title: "Update Category",
      requiresAuth: true,
    },
    path: "/update-category/:categoryId/",
    name: "update-category",
    component: UpdateCategory,
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
