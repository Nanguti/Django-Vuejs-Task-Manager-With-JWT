<template>
  <div class="hidden md:flex flex-col w-64 bg-gray-800">
    <div class="flex items-center justify-center h-16 bg-gray-900">
      <span class="text-white font-bold uppercase">APHRC</span>
    </div>
    <div class="flex flex-col flex-1 overflow-y-auto">
      <nav class="flex-1 px-2 py-4 bg-gray-800">
        <router-link
          to="/"
          class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700"
        >
          <ChartBarIcon class="w-5 h-5 hover:cursor-pointer mx-2" />

          Dashboard
        </router-link>
        <router-link
          to="/users/"
          class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700"
        >
          <UserIcon class="w-5 h-5 hover:cursor-pointer mx-2" />
          Users
        </router-link>
        <router-link
          to="/categories/"
          class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700"
        >
          <FolderIcon class="w-5 h-5 hover:cursor-pointer mx-2" />
          Categories
        </router-link>
        <router-link
          to="/"
          class="flex items-center px-4 py-2 text-gray-100 hover:bg-gray-700"
        >
          <CheckCircleIcon class="w-5 h-5 hover:cursor-pointer mx-2" />
          Tasks
        </router-link>

        <router-link
          to="/logout"
          class="flex items-center px-4 py-2 mt-2 text-gray-100 hover:bg-gray-700"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6 mr-2"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 10V3L4 14h7v7l9-11h-7z"
            />
          </svg>
          Settings
        </router-link>
      </nav>
    </div>
  </div>
</template>

<script setup>
import {
  UserIcon,
  FolderIcon,
  ChartBarIcon,
  CheckCircleIcon,
} from "@heroicons/vue/24/outline";
</script>
