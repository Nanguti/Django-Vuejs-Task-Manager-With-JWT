import { ref } from "vue";
import axiosClient from "../axios";
import { useRouter } from "vue-router";
import { useToast } from "vue-toast-notification";

export default function useTask() {
  const tasks = ref([]);
  const router = useRouter();
  const $toast = useToast();

  const fetchTasks = async () => {
    try {
      const response = await axiosClient.get("/tasks/");
      tasks.value = response.data;
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
    completeTask,
    deleteTask,
    goToTaskDetail,
    goToUpdatePage,
  };
}
