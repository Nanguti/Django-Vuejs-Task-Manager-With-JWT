import { ref } from "vue";
import axiosClient from "../axios";
import { useRouter } from "vue-router";
import { useToast } from "vue-toast-notification";

export default function useTask() {
  const users = ref([]);
  const router = useRouter();
  const $toast = useToast();
  const resultsPerPage = ref(0);
  const totalCount = ref(0);
  const currentPage = ref(1);
  const totalPages = ref(0);
  const pageSize = 10;

  const addUser = async (formData) => {
    const response = await axiosClient.post("/users/", formData);
    if (response.status === 201 && response.data.id) {
      router.push("/users");
    }
  };

  const getUsers = async (pageNumber = 1) => {
    try {
      const response = await axiosClient.get(`/users/?page=${pageNumber}`);
      users.value = response.data.results;
      resultsPerPage.value = response.data.results.length;
      totalCount.value = response.data.count;
      currentPage.value = pageNumber;
      totalPages.value = Math.ceil(response.data.count / pageSize);
    } catch (error) {
      console.error("Error fetching tasks:", error);
    }
  };

  const removeUser = async (userId) => {
    try {
      const confirmed = window.confirm(
        "Are you sure you want to delete this task?"
      );
      if (confirmed) {
        await axiosClient.delete(`/users/${userId}`);
        $toast.success("User Successfully deleted!");
        getUsers();
      }
    } catch (error) {
      console.error("Error deleting task:", error);
      $toast.error("Error removing the  user");
    }
  };

  const userDetail = (userId) => {
    router.push({ name: "user-detail", params: { userId } });
  };

  const goToUpdatePage = (userId) => {
    router.push(`/update-iser/${userId}`);
  };

  return {
    users,
    addUser,
    getUsers,
    totalCount,
    currentPage,
    totalPages,
    resultsPerPage,
    removeUser,
    userDetail,
    goToUpdatePage,
  };
}
