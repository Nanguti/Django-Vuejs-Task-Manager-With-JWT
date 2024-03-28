import { ref } from "vue";
import axiosClient from "../axios";
import { useRouter } from "vue-router";
import { useToast } from "vue-toast-notification";

export default function useTask() {
  const categories = ref([]);
  const router = useRouter();
  const $toast = useToast();
  const resultsPerPage = ref(0);
  const totalCount = ref(0);
  const currentPage = ref(1);
  const totalPages = ref(0);
  const pageSize = 10;

  const addCategory = async (formData) => {
    const response = await axiosClient.post("/categories/", formData);
    if (response.status === 201 && response.data.id) {
      categoryDetail(response.data.id);
    }
  };

  const getCategories = async (pageNumber = 1) => {
    try {
      const response = await axiosClient.get(`/categories/`);
      categories.value = response.data.results;
      resultsPerPage.value = response.data.results.length;
      totalCount.value = response.data.count;
      currentPage.value = pageNumber;
      totalPages.value = Math.ceil(response.data.count / pageSize);
    } catch (error) {
      console.error("Error fetching Category:", error);
    }
  };

  const deleteCategory = async (categoryId) => {
    try {
      const confirmed = window.confirm(
        "Are you sure you want to delete this category?"
      );
      if (confirmed) {
        await axiosClient.delete(`/categories/${categoryId}`);
        $toast.success("Category Successfully deleted!");
        getCategories();
      }
    } catch (error) {
      console.error("Error deleting task:", error);
      $toast.error("Error deleting the  category");
    }
  };

  const goToUpdatePage = (categoryId) => {
    router.push(`/update-task/${categoryId}`);
  };

  return {
    categories,
    addCategory,
    getCategories,
    totalCount,
    currentPage,
    totalPages,
    resultsPerPage,
    deleteCategory,
    categoryDetail,
    goToUpdatePage,
  };
}
