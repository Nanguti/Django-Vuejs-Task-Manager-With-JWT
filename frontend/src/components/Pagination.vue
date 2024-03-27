<template>
  <div
    class="flex items-center justify-between border-t border-gray-200 bg-white px-4 py-3 sm:px-6"
  >
    <div class="flex flex-1 justify-between sm:hidden">
      <a
        href="#"
        @click="goToPage(currentPage - 1)"
        class="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
        :disabled="currentPage === 1"
      >
        Previous
      </a>
      <a
        href="#"
        @click="goToPage(currentPage + 1)"
        class="relative ml-3 inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
        :disabled="currentPage === totalPages"
      >
        Next
      </a>
    </div>
    <div class="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
      <div>
        <p class="text-sm text-gray-700">
          Showing
          {{ " " }}
          <span class="font-medium">{{ startIndex }}</span>
          {{ " " }}
          to
          {{ " " }}
          <span class="font-medium">{{ endIndex }}</span>
          {{ " " }}
          of
          {{ " " }}
          <span class="font-medium">{{ totalCount }}</span>
          {{ " " }}
          results
        </p>
      </div>
      <div>
        <nav
          class="isolate inline-flex -space-x-px rounded-md shadow-sm"
          aria-label="Pagination"
        >
          <a
            href="#"
            @click="goToPage(currentPage - 1)"
            class="relative inline-flex items-center rounded-l-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
            :disabled="currentPage === 1"
          >
            <span class="sr-only">Previous</span>
            <ChevronLeftIcon class="h-5 w-5" aria-hidden="true" />
          </a>

          <div v-for="(pageNumber, index) in visiblePages" :key="index">
            <a
              href="#"
              @click="goToPage(pageNumber)"
              :class="{
                'bg-indigo-600 text-white': pageNumber === currentPage,
              }"
              class="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
            >
              {{ pageNumber }}
            </a>
          </div>

          <a
            href="#"
            @click="goToPage(currentPage + 1)"
            class="relative inline-flex items-center rounded-r-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
            :disabled="currentPage === totalPages"
          >
            <span class="sr-only">Next</span>
            <ChevronRightIcon class="h-5 w-5" aria-hidden="true" />
          </a>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, defineProps, defineEmits } from "vue";
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/vue/20/solid";

const props = defineProps({
  totalCount: {
    type: Number,
    required: true,
  },
  currentPage: {
    type: Number,
    required: true,
  },
  totalPages: {
    type: Number,
    required: true,
  },
  resultsPerPage: {
    type: Number,
    required: true,
  },
});

const emit = defineEmits(["goToPage"]);
const goToPage = (pageNumber) => {
  if (pageNumber > 0 && pageNumber <= props.totalPages) {
    emit("goToPage", pageNumber);
  }
};

const visiblePages = computed(() => {
  const totalVisiblePages = 5;
  const startPage = Math.max(
    1,
    props.currentPage - Math.floor(totalVisiblePages / 2)
  );
  const endPage = Math.min(props.totalPages, startPage + totalVisiblePages - 1);
  return Array.from(
    { length: endPage - startPage + 1 },
    (_, i) => startPage + i
  );
});

const startIndex = computed(() => {
  return (props.currentPage - 1) * props.resultsPerPage + 1;
});

const endIndex = computed(() => {
  const lastItemIndex = props.currentPage * props.resultsPerPage;
  return Math.min(lastItemIndex, props.totalCount);
});
</script>
