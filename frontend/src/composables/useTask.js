import { ref } from "vue";
import axiosClient from "../axios";
import { useRouter } from "vue-router";
import { useToast } from "vue-toast-notification";

export default function useTask() {
  const tasks = ref([]);
  const router = useRouter();
  const $toast = useToast();
  const taskCount = ref(0);
  const totalCount = ref(0);
  const currentPage = ref(1);
  const totalPages = ref(0);
  const pageSize = 3;

  const fetchTasks = async (pageNumber = 1) => {
    try {
      const response = await axiosClient.get(`/tasks/?page=${pageNumber}`);
      tasks.value = response.data.results;
      totalCount.value = response.data.count;
      currentPage.value = pageNumber;
      totalPages.value = Math.ceil(response.data.count / pageSize);
    } catch (error) {
      console.error("Error fetching tasks:", error);
    }
  };

  const completeTask = async (taskId) => {
    try {
      await axiosClient.patch(`/tasks/${taskId}/`, { completed: true });
      $toast.success("Task status updated successfully!");
      fetchTasks();
    } catch (error) {
      console.error("Error completing task:", error);
    }
  };

  const deleteTask = async (taskId) => {
    try {
      const confirmed = window.confirm(
        "Are you sure you want to delete this task?"
      );
      if (confirmed) {
        await axiosClient.delete(`/tasks/${taskId}`);
        $toast.success("Task Successfully deleted!");
        fetchTasks();
      }
    } catch (error) {
      console.error("Error deleting task:", error);
      $toast.error("Error deleting task");
    }
  };

  const goToTaskDetail = (taskId) => {
    router.push({ name: "task-detail", params: { taskId } });
  };

  const goToUpdatePage = (taskId) => {
    router.push(`/update-task/${taskId}`);
  };

  return {
    tasks,
    fetchTasks,
    totalCount,
    currentPage,
    totalPages,
    completeTask,
    deleteTask,
    goToTaskDetail,
    goToUpdatePage,
  };
}
