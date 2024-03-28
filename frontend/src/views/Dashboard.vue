<template>
  <AuthenticatedLayout>
    <div class="p-4">
      <div
        class="max-w-[90%] mx-auto my-10 bg-white p-8 rounded-xl shadow shadow-slate-300"
      >
        <div class="flex flex-row justify-between items-center">
          <div>
            <h1 class="text-3xl font-medium">Tasks list</h1>
          </div>
          <div class="inline-flex space-x-2 items-center">
            <router-link
              to="/create-task"
              class="p-2 border border-slate-200 rounded-md inline-flex space-x-1 items-center text-white hover:text-white bg-indigo-600 hover:bg-indigo-500"
            >
              <PlusCircleIcon
                class="w-4 h-4 text-white hover:text-slate-700 hover:cursor-pointer"
              />
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
          <table class="min-w-full divide-y divide-gray-200">
            <thead>
              <tr>
                <th
                  class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Task Title
                </th>
                <th
                  class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Assignee
                </th>
                <th
                  class="px-6 py-3 bg-gray-50 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  Due Date
                </th>
                <th class="px-6 py-3 bg-gray-50">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="task in tasks" :key="task.id" class="bg-white">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <div class="flex-shrink-0 h-6 w-6">
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
                    <div class="ml-4">
                      <div :class="{ 'line-through': task.completed }">
                        {{ task.title }}
                      </div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900">{{ task.owner_name }}</div>
                </td>

                <td class="px-6 py-4 whitespace-nowrap">
                  <div
                    :class="{
                      'text-green-600': task.completed,
                      'text-red-600':
                        !task.completed && isPastDue(task.due_date),
                    }"
                    class="text-sm"
                  >
                    {{ formattedDueDate(task.due_date) }}
                  </div>
                </td>

                <td
                  class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium"
                >
                  <div class="flex items-center">
                    <input
                      type="checkbox"
                      class="ml-2 h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
                      :id="'toggle-' + task.id"
                      @change="handleCompleteTask(task.id)"
                      :checked="task.completed"
                    />
                    <label :for="'toggle-' + task.id" class="ml-1 text-gray-700"
                      >Complete</label
                    >
                    <EyeIcon
                      @click="handleTaskDetail(task.id)"
                      class="w-5 h-5 text-indigo-700 hover:text-indigo-700 hover:cursor-pointer mx-2"
                    >
                      View
                    </EyeIcon>
                    <PencilIcon
                      @click="handleUpdateTask(task.id)"
                      class="h-5 w-5 text-gray-500 hover:cursor-pointer mr-2"
                    >
                      Edit
                    </PencilIcon>

                    <div v-if="user.is_superuser" class="ml-2">
                      <TrashIcon
                        @click="handleDeleteTask(task.id)"
                        class="w-4 h-4 text-red-700 hover:text-slate-700 hover:cursor-pointer"
                      >
                        Delete
                      </TrashIcon>
                    </div>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
        <Pagination
          :totalCount="totalCount"
          :currentPage="currentPage"
          :totalPages="totalPages"
          :resultsPerPage="resultsPerPage"
          @goToPage="fetchTasks"
        />
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
import Pagination from "../components/Pagination.vue";
import {
  TrashIcon,
  EyeIcon,
  PencilIcon,
  PlusCircleIcon,
} from "@heroicons/vue/24/outline";

const {
  tasks,
  fetchTasks,
  completeTask,
  deleteTask,
  goToTaskDetail,
  goToUpdatePage,
  totalCount,
  currentPage,
  totalPages,
  resultsPerPage,
} = useTask();

const user = JSON.parse(localStorage.getItem("userData"));

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
const formattedDueDate = (dueDate) => {
  const date = new Date(dueDate);
  return date.toLocaleString();
};
const isPastDue = (dueDate) => {
  const today = new Date();
  const due = new Date(dueDate);
  return due < today;
};
onMounted(fetchTasks);
</script>
