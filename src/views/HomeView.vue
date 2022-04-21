<template>
	<section class="w-11/12">
		<SearchBar />

		<section class="w-full my-8" v-for="word in words" :key="word.id">
			<h1 class="font-bold text-xl">{{ word.word }}</h1>
			<div class="ml-4">
				<p class="lowercase text-gray-500 italic text-lg">{{ word.part_of_speech }}</p>
				<p class="">{{ word.description }}</p>
				<p class="font-light text-gray-700">"{{ word.inSentence}}"</p>
			</div>
		</section>
	</section>
</template>

<script>
// @ is an alias to /src
import SearchBar from "@/components/search_bar.vue";

import axios from "axios";

export default {
  name: "HomeView",
  components: {
    SearchBar,
  },
  data() {
    return {
      words: [],
    };
  },
  mounted() {
    this.getWords();
  },
  methods: {
    getWords() {
      axios({
        method: "get",
        url: "http://192.168.0.108:8000/word",
        auth: {
          username: "skye",
          password: "1234",
        },
      }).then((response) => (this.words = response.data));
    },
  },
};
</script>
