<template>
  <AuthenticatedLayout>
    <form @submit.prevent="addCategory">
      <div class="p-8 space-y-12 max-w-[50%] mx-auto">
        <div class="border-b border-gray-900/10 pb-12">
          <h2 class="text-base font-semibold leading-7 text-gray-900">
            Add Category
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
                  v-model="formData.name"
                  autocomplete="title"
                  class="p-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
                />
              </div>
            </div>
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
import AuthenticatedLayout from "../../layouts/AuthenticatedLayout.vue";
import axiosClient from "../../axios";
import { useRouter } from "vue-router";
import { useToast } from "vue-toast-notification";
import "vue-toast-notification/dist/theme-sugar.css";

const $toast = useToast();
const router = useRouter();
const userData = JSON.parse(localStorage.getItem("userData"));
const isSuperUser = userData.is_superuser;

const formData = {
  name: "",
};

const addCategory = async () => {
  try {
    await axiosClient.post("/categories/", formData);
    $toast.success("Category Successfully Added!");
    router.push("/categories/");
  } catch (error) {
    console.error("Error adding Catgory:", error);
  }
};

const cancel = () => {
  router.push("/");
};
</script>
