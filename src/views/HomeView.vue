<template>
	<main class="flex flex-col justify-center items-center w-full">
		<SearchBar :search="search" />
    <Content :words="words"/>
		
	</main>
</template>

<script>
// @ is an alias to /src
import SearchBar from "@/components/search_bar.vue";
import Content from "@/components/content.vue";

import axios from "axios";

export default {
  name: "HomeView",
  components: {
    SearchBar,
    Content
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
        url: "http://localhost:8000/word",
        auth: {
          username: "skye",
          password: "1234",
        },
      }).then((response) => (this.words = response.data));
    },
    search(term) { 
      // this.resetWord()/
      this.words = this.words.filter((words) => {
        return words.word.toLowerCase().includes(term.toLowerCase())
      })
    },

    // resetWord() {
    //   this.word = this.words
    // }
  },
};
</script>
