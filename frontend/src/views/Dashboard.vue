<template>
  <AuthenticatedLayout>
    <div class="p-4">
      <div
        class="max-w-[75%] mx-auto my-10 bg-white p-8 rounded-xl shadow shadow-slate-300"
      >
        <div class="flex flex-row justify-between items-center">
          <div>
            <h1 class="text-3xl font-medium">Tasks list</h1>
          </div>
          <div class="inline-flex space-x-2 items-center">
            <router-link
              to="/create-task"
              class="p-2 border border-slate-200 rounded-md inline-flex space-x-1 items-center text-indigo-200 hover:text-white bg-indigo-600 hover:bg-indigo-500"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-4 h-4"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              <span class="text-sm font-medium hidden md:block">Add Task</span>
            </router-link>
          </div>
        </div>

        <div id="tasks" class="my-5">
          <div
            v-if="tasks.length === 0"
            class="text-center font-semibold text-gray-500"
          >
            You do not have tasks at the moment! Would like to create one?
          </div>
          <div
            v-else
            v-for="task in tasks"
            :key="task.id"
            class="flex justify-between items-center border-b border-slate-200 py-3 px-2 border-l-4 border-l-transparent bg-gradient-to-r from-transparent to-transparent hover:from-slate-100 transition ease-linear duration-150"
          >
            <div class="inline-flex items-center space-x-2">
              <div>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6 text-slate-500"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M4.5 12.75l6 6 9-13.5"
                  />
                </svg>
              </div>
              <div :class="{ 'line-through': task.completed }">
                {{ task.title }}
              </div>
            </div>
            <div class="flex items-center">
              <EyeIcon
                @click="handleTaskDetail(task.id)"
                class="h-8 w-8 mx-2 text-gray-500 hover:cursor-pointer"
                aria-hidden="true"
              />

              <PencilIcon
                @click="handleUpdateTask(task.id)"
                class="h-5 w-5 mx-3 text-gray-500 hover:cursor-pointer"
                aria-hidden="true"
              />

              <input
                type="checkbox"
                class="peer sr-only opacity-0"
                :id="'toggle-' + task.id"
                @change="handleCompleteTask(task.id)"
                :checked="task.completed"
              />
              <label
                :for="'toggle-' + task.id"
                :class="{
                  'bg-green-500': task.completed,
                  'bg-gray-400': !task.completed,
                  'mr-1': task.completed,
                }"
                class="relative flex h-6 w-11 cursor-pointer items-center rounded-full px-0.5 outline-gray-400 transition-colors before:h-5 before:w-5 before:rounded-full before:bg-white before:shadow before:transition-transform before:duration-300 peer-focus-visible:outline peer-focus-visible:outline-offset-2 peer-focus-visible:outline-gray-400 peer-checked:peer-focus-visible:outline-green-500"
              >
                <span class="sr-only">Enable</span>
              </label>
              <XMarkIcon class="h-6 w-6" aria-hidden="true" />

              <TrashIcon
                class="w-4 h-4 text-slate-500 hover:text-slate-700 hover:cursor-pointer"
                @click="handleDeleteTask(task.id)"
              />
            </div>
          </div>
        </div>
        <!-- <Pagination
          :totalCount="totalCount"
          :currentPage="currentPage"
          :totalPages="totalPages"
          @goToPage="getPosts"
        /> -->
        <!-- <p class="text-xs text-slate-500 text-center">
          Last updated 
        </p> -->
      </div>
    </div>
  </AuthenticatedLayout>
</template>

<script setup>
import useTask from "../composables/useTask";
import { onMounted } from "vue";
import AuthenticatedLayout from "../layouts/AuthenticatedLayout.vue";
import { TrashIcon, EyeIcon, PencilIcon } from "@heroicons/vue/24/outline";
const {
  tasks,
  fetchTasks,
  completeTask,
  deleteTask,
  goToTaskDetail,
  goToUpdatePage,
} = useTask();

const handleCompleteTask = (taskId) => {
  completeTask(taskId);
};

const handleDeleteTask = (taskId) => {
  deleteTask(taskId);
};

const handleTaskDetail = (taskId) => {
  goToTaskDetail(taskId);
};

const handleUpdateTask = (taskId) => {
  goToUpdatePage(taskId);
};

onMounted(fetchTasks);
</script>
