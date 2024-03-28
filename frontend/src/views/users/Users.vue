<template>
  <AuthenticatedLayout>
    <div class="p-4">
      <div
        class="max-w-[90%] mx-auto my-10 bg-white p-8 rounded-xl shadow shadow-slate-300"
      >
        <div class="flex flex-row justify-between items-center">
          <div>
            <h1 class="text-3xl font-medium">Users List</h1>
          </div>
          <div class="inline-flex space-x-2 items-center">
            <router-link
              to="/create-task"
              class="p-2 border border-slate-200 rounded-md inline-flex space-x-1 items-center text-white hover:text-white bg-indigo-600 hover:bg-indigo-500"
            >
              <PlusCircleIcon
                class="w-4 h-4 text-white hover:text-slate-700 hover:cursor-pointer"
              />
              <span class="text-sm font-medium hidden md:block">Add User</span>
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
                        Username
                      </th>
                      <th
                        scope="col"
                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left"
                      >
                        Email
                      </th>
                      <th
                        scope="col"
                        class="text-sm font-medium text-gray-900 px-6 py-4 text-left"
                      >
                        IS Admin
                      </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(user, index) in users"
                      :key="user.id"
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
                        {{ user.username }}
                      </td>
                      <td
                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                      >
                        {{ user.email }}
                      </td>
                      <td
                        class="text-sm text-gray-900 font-light px-6 py-4 whitespace-nowrap"
                      >
                        {{ user.is_superuser }}
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </AuthenticatedLayout>
</template>

<script setup>
import { PlusCircleIcon } from "@heroicons/vue/24/outline";
import AuthenticatedLayout from "../../layouts/AuthenticatedLayout.vue";
import useUser from "../../composables/useUser";
import { onMounted } from "vue";

const { users, getUsers } = useUser();
onMounted(getUsers);
</script>
