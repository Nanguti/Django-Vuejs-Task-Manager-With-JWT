<template>
  <AuthenticatedLayout>
    <div class="p-4">
      <div
        class="max-w-[75%] mx-auto my-10 bg-white p-8 rounded-xl shadow shadow-slate-300"
      >
        <div class="flex flex-row justify-between items-center">
          <div>
            <h1 class="text-3xl font-medium">Category List</h1>
          </div>
          <div class="inline-flex space-x-2 items-center">
            <router-link
              to="/create-category"
              class="p-2 border border-slate-200 rounded-md inline-flex space-x-1 items-center text-white hover:text-white bg-indigo-600 hover:bg-indigo-500"
            >
              <PlusCircleIcon
                class="w-4 h-4 text-white hover:text-slate-700 hover:cursor-pointer"
              />
              <span class="text-sm font-medium hidden md:block"
                >Add Category</span
              >
            </router-link>
          </div>
        </div>
        <div class="flex flex-col">
          <div class="overflow-x-auto sm:-mx-6 lg:-mx-8">
            <div class="py-2 inline-block min-w-full sm:px-6 lg:px-8">
              <div class="overflow-hidden">
                <table class="min-w-full">
                  <thead class="border-b">
                    <tr>
                      <th
                        scope="col"
                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left"
                      >
                        ID
                      </th>
                      <th
                        scope="col"
                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left"
                      >
                        Name
                      </th>
                      <th
                        scope="col"
                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left"
                      >
                        Actions
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(category, index) in categories"
                      :key="category.id"
                      class="border-b"
                    >
                      <td
                        class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
                      >
                        {{ index + 1 }}
                      </td>
                      <td
                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                      >
                        {{ category.name }}
                      </td>
                      <td
                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                      >
                        <div class="flex items-center">
                          <PencilIcon
                            @click="handleUpdateCategory(category.id)"
                            class="h-5 w-5 text-gray-500 hover:cursor-pointer mr-2"
                          >
                            Edit
                          </PencilIcon>

                          <div v-if="user.is_superuser" class="ml-2">
                            <TrashIcon
                              @click="handleDeleteCategory(category.id)"
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
                <Pagination
                  :totalCount="totalCount"
                  :currentPage="currentPage"
                  :totalPages="totalPages"
                  :resultsPerPage="resultsPerPage"
                  @goToPage="fetchTasks"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AuthenticatedLayout>
</template>

<script setup>
import {
  PlusCircleIcon,
  TrashIcon,
  PencilIcon,
} from "@heroicons/vue/24/outline";
import AuthenticatedLayout from "../../layouts/AuthenticatedLayout.vue";
import Pagination from "../../components/Pagination.vue";
import useCategory from "../../composables/useCategory";
import { onMounted } from "vue";

const user = JSON.parse(localStorage.getItem("userData"));

const {
  categories,
  getCategories,
  totalCount,
  currentPage,
  totalPages,
  resultsPerPage,
  deleteCategory,
  goToUpdatePage,
} = useCategory();

const handleDeleteCategory = (categoryId) => {
  deleteCategory(categoryId);
};

const handleUpdateCategory = (categoryId) => {
  goToUpdatePage(categoryId);
};

onMounted(getCategories);
</script>
