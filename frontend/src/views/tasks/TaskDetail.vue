<template>
  <AuthenticatedLayout>
    <div class="p-8">
      <div
        v-if="taskDetail"
        class="bg-white overflow-hidden shadow rounded-lg border p-8"
      >
        <div class="px-4 py-5 sm:px-6 flex items-center justify-between">
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            <router-link
              class="group flex font-semibold text-sm leading-6 text-slate-700 hover:text-slate-900 dark:text-slate-200 dark:hover:text-white"
              to="/"
            >
              <svg
                viewBox="0 -9 3 24"
                class="overflow-visible mr-3 text-slate-400 w-auto h-6 group-hover:text-slate-600 dark:group-hover:text-slate-300"
              >
                <path
                  d="M3 0L0 3L3 6"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                ></path>
              </svg>
              Go Back To Task List
            </router-link>
          </h3>
          <PencilIcon
            @click="goToUpdatePage(taskDetail.id)"
            class="h-5 w-5 mx-3 text-gray-500 hover:cursor-pointer"
            aria-hidden="true"
          />
        </div>

        <div class="border-t border-gray-200 px-4 py-5 sm:p-0">
          <dl class="sm:divide-y sm:divide-gray-200">
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">Title</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ taskDetail.title }}
              </dd>
            </div>

            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">Category Nme</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ taskDetail.category_name }}
              </dd>
            </div>

            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">Owner Nme</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ taskDetail.owner_name }}
              </dd>
            </div>
            <div class="py-3 sm:py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
              <dt class="text-sm font-medium text-gray-500">Description</dt>
              <dd class="mt-1 text-sm text-gray-900 sm:mt-0 sm:col-span-2">
                {{ taskDetail.description }}
              </dd>
            </div>
          </dl>
        </div>
      </div>
      <div v-else>Loading...</div>
    </div>
  </AuthenticatedLayout>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import AuthenticatedLayout from "../../layouts/AuthenticatedLayout.vue";
import axiosClient from "../../axios";
import { PencilIcon } from "@heroicons/vue/24/outline";
import { useRouter } from "vue-router";
const router = useRouter();
const taskDetail = ref(null);
const accessToken = localStorage.getItem("accessToken");
const route = useRoute();

const fetchTaskDetail = async () => {
  try {
    const taskId = route.params.taskId;
    const response = await axiosClient.get(`/tasks/${taskId}/detail`);
    taskDetail.value = response.data;
  } catch (error) {
    console.error("Error fetching task detail:", error);
  }
};

const goToUpdatePage = (taskId) => {
  router.push(`/update-task/${taskId}`);
};

onMounted(fetchTaskDetail);
</script>
