<template>
  <AuthenticatedLayout>
    <form @submit.prevent="updateTask">
      <div class="p-8 space-y-12 max-w-[50%] mx-auto">
        <div class="border-b border-gray-900/10 pb-12">
          <h2 class="text-base font-semibold leading-7 text-gray-900">
            Update Task
          </h2>

          <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
            <div class="col-span-full">
              <label
                for="title"
                class="block text-sm font-medium leading-6 text-gray-900"
                >Title</label
              >
              <div class="mt-2">
                <input
                  type="text"
                  name="title"
                  id="title"
                  v-model="formData.title"
                  autocomplete="title"
                  class="p-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div class="col-span-full">
              <label
                for="category"
                class="block text-sm font-medium leading-6 text-gray-900"
                >Category</label
              >
              <div class="mt-2">
                <select
                  id="category"
                  name="category"
                  v-model="formData.category"
                  class="p-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                >
                  <option value="" disabled selected>Select Category</option>
                  <option
                    v-for="category in categories"
                    :key="category.id"
                    :value="category.id"
                  >
                    {{ category.name }}
                  </option>
                </select>
              </div>
              <p class="mt-1 text-xs text-gray-600">Or</p>
              <div class="mt-2">
                <input
                  type="text"
                  name="newCategory"
                  id="newCategory"
                  v-model="newCategory"
                  placeholder="New Category"
                  class="p-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>

            <div class="col-span-full">
              <label
                for="about"
                class="block text-sm font-medium leading-6 text-gray-900"
                >Description</label
              >
              <div class="mt-2">
                <textarea
                  id="about"
                  name="about"
                  v-model="formData.description"
                  rows="3"
                  class="p-2 block w-full rounded-md py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                ></textarea>
              </div>
              <p class="mt-3 text-sm leading-6 text-gray-600">
                Write a few sentences about task.
              </p>
            </div>

            <!-- Dropdown for selecting user to assign task -->
            <div v-if="isSuperUser" class="col-span-full">
              <label
                for="assignee"
                class="block text-sm font-medium leading-6 text-gray-900"
                >Assign To</label
              >
              <div class="mt-2">
                <select
                  id="assignee"
                  name="assignee"
                  v-model="formData.assignee"
                  class="p-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                >
                  <option v-for="user in users" :key="user.id" :value="user.id">
                    {{ user.username }}
                  </option>
                </select>
              </div>
            </div>

            <label for="dueDate">Due Date:</label>
            <datepicker
              v-model="dueDate"
              format="yyyy-MM-dd"
              :clear-button="true"
            ></datepicker>
          </div>
        </div>
      </div>

      <div
        class="mt-6 flex items-center justify-end gap-x-6 max-w-[50%] mx-auto"
      >
        <button
          @click="cancel"
          type="button"
          class="text-sm font-semibold leading-6 text-gray-900"
        >
          Cancel
        </button>
        <button
          type="submit"
          class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
        >
          Save
        </button>
      </div>
    </form>
  </AuthenticatedLayout>
</template>

<script setup>
import AuthenticatedLayout from "../layouts/AuthenticatedLayout.vue";
import axiosClient from "../axios";
import { useRouter } from "vue-router";
import { ref, onMounted } from "vue";
import { useToast } from "vue-toast-notification";
import "vue-toast-notification/dist/theme-sugar.css";
const $toast = useToast();

const router = useRouter();
const userData = JSON.parse(localStorage.getItem("userData"));
const isSuperUser = userData.is_superuser;

const formData = {
  title: "",
  description: "",
  owner: userData.id,
  completed: false,
  assignee: isSuperUser ? null : userData.id,
  category: "",
};

const newCategory = ref("");
const categories = ref([]);

const fetchCategories = async () => {
  try {
    const accessToken = localStorage.getItem("accessToken");
    axiosClient.defaults.headers.common[
      "Authorization"
    ] = `Token ${accessToken}`;

    const response = await axiosClient.get("/categories/");
    return response.data;
  } catch (error) {
    console.error("Error fetching categories:", error);
    return [];
  }
};

const updateTask = async () => {
  try {
    const accessToken = localStorage.getItem("accessToken");
    axiosClient.defaults.headers.common[
      "Authorization"
    ] = `Token ${accessToken}`;
    if (newCategory.value.trim() !== "") {
      const response = await axiosClient.post("/categories/", {
        name: newCategory.value.trim(),
      });
      formData.category = response.data.id;
    }
    if (isSuperUser && formData.assignee) {
      formData.owner = formData.assignee;
    }

    const response = await axiosClient.put(`/tasks/${taskId}`, formData); // Replace `taskId` with the actual task ID
    $toast.success("Task Successfully Updated!");
    router.push("/");
  } catch (error) {
    console.error("Error updating task:", error);
  }
};

const cancel = () => {
  router.push("/");
};

onMounted(async () => {
  categories.value = await fetchCategories();
});
</script>
