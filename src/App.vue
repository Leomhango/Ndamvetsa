<template>
  
  <nav class="flex flex-row justify-center items-center py-4 shadow-md ">
    <router-link class="text-2xl font-semibold text-blue-500" to="/">Ndamvetsa</router-link>
  </nav>
  <main class="flex flex-col justify-center items-center w-full my-8">
    <router-view class="flex flex-col items-center justify-center w-10/12 "/>
  </main>
</template>