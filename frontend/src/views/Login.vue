<template>
  <div>
    <GuestLayout>
      <div
        class="h-screen bg-gradient-to-r from-gray-100 via-[#bce1ff] to-gray-100 flex justify-center items-center w-full"
      >
        <form @submit.prevent="login">
          <div
            class="bg-white px-10 py-8 rounded-xl w-screen shadow-xl max-w-sm"
          >
            <div class="space-y-4">
              <h1 class="text-center text-2xl font-semibold text-gray-600">
                Login
              </h1>

              <hr />
              <div v-if="errorMessage" class="text-red-500 mt-2">
                {{ errorMessage }}
              </div>
              <div class="flex items-center border-2 py-2 px-3 rounded-md mb-4">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-400"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"
                  />
                </svg>
                <input
                  class="pl-2 outline-none border-none w-full"
                  v-model="formData.username"
                  type="username"
                  name="username"
                  value=""
                  placeholder="username"
                  required
                />
              </div>
              <div class="flex items-center border-2 py-2 px-3 rounded-md">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-5 w-5 text-gray-400"
                  viewBox="0 0 20 20"
                  fill="currentColor"
                >
                  <path
                    fill-rule="evenodd"
                    d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                    clip-rule="evenodd"
                  />
                </svg>
                <input
                  class="pl-2 outline-none border-none w-full"
                  v-model="formData.password"
                  type="password"
                  name="password"
                  id=""
                  placeholder="Password"
                  required
                />
              </div>
            </div>
            <!-- Remember Me checkbox -->
            <div class="flex justify-center items-center mt-4">
              <p
                class="inline-flex items-center text-gray-700 font-medium text-xs text-center"
              >
                <input
                  type="checkbox"
                  id="rememberMeCheckbox"
                  name="rememberMe"
                  class="mr-2"
                />
                <span class="text-xs font-semibold">Remember me?</span>
              </p>
            </div>

            <button
              type="submit"
              value="login"
              id="login"
              class="mt-6 w-full shadow-xl bg-gradient-to-tr from-blue-600 to-red-400 hover:to-red-700 text-indigo-100 py-2 rounded-md text-lg tracking-wide transition duration-1000"
            >
              Login
            </button>
            <hr />
            <div class="flex justify-center items-center mt-4">
              <p
                class="inline-flex items-center text-gray-700 font-medium text-xs text-center"
              >
                <span class="ml-2"
                  >You don't have an account?<router-link
                    to="/register"
                    class="text-xs ml-2 text-blue-500 font-semibold"
                    >Register now &rarr;</router-link
                  >
                </span>
              </p>
            </div>
          </div>
          <div class="pt-6 text-base font-semibold leading-7">
            <p
              class="font-sans font-semibold text-red-500 text-md hover:text-red-800"
            >
              <router-link to="/" class="absolute">&larr; Home</router-link>
            </p>
          </div>
        </form>
      </div>
    </GuestLayout>
  </div>
</template>
<script setup>
import GuestLayout from "../layouts/GuestLayout.vue";
import axiosClient from "../axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();
const formData = {
  username: "",
  password: "",
};
const errorMessage = ref("");

const login = async () => {
  try {
    const response = await axiosClient.post("/auth/token/login/", formData);
    if (response.status === 200 && response.data.auth_token) {
      localStorage.setItem("accessToken", response.data.auth_token);
      const userResponse = await axiosClient.get("/auth/users/me/");
      if (userResponse.status === 200) {
        const userData = userResponse.data;
        localStorage.setItem("userData", JSON.stringify(userData));

        router.push("/");
      } else {
        console.error("Error retrieving user data:", userResponse.data);
      }
    }
  } catch (error) {
    errorMessage.value = error.response.data.non_field_errors[0];
  }
};
</script>
