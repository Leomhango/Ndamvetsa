<template>
  
  <nav class="flex flex-row justify-between px-10 items-center py-4 shadow-md">
    <router-link class="text-2xl font-semibold text-blue-500" to="/">Ndamvetsa</router-link>
    <router-link class="bg-blue-500 px-5 py-2 rounded-md text-white" to="/signup">Sign In</router-link>
  </nav>
  
  <router-view class=""/>
</template>