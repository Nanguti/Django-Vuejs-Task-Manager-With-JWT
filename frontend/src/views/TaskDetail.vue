<template>
  <AuthenticatedLayout>
    <div class="p-8">
      <div
        v-if="taskDetail"
        class="bg-white overflow-hidden shadow rounded-lg border p-8"
      >
        <div class="px-4 py-5 sm:px-6">
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Task Details
          </h3>
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
import AuthenticatedLayout from "../layouts/AuthenticatedLayout.vue";
import axiosClient from "../axios";

const taskDetail = ref(null);
const accessToken = localStorage.getItem("accessToken");
const route = useRoute();

const fetchTaskDetail = async () => {
  try {
    axiosClient.defaults.headers.common[
      "Authorization"
    ] = `Token ${accessToken}`;
    const taskId = route.params.taskId;
    const response = await axiosClient.get(`/tasks/${taskId}/detail`);
    taskDetail.value = response.data;
    console.log(response.data);
  } catch (error) {
    console.error("Error fetching task detail:", error);
  }
};

onMounted(fetchTaskDetail);
</script>
