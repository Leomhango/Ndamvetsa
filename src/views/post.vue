<template>
    <main class="flex flex-col justify-center items-center w-full my-10">
        <form 
            action="" 
            class="flex flex-col justify-center items-center w-10/12 space-y-4"
            v-on:submit.prevent="addWord"
        >
            <input 
                v-model="word"
                type="text" 
                placeholder="Enter word" 
                name="word" id="" 
                class="bg-blue-50 w-full py-3 px-4 rounded outline-blue-500"
            >
            <input 
                v-model="pos"
                type="text" 
                placeholder="Enter Part of Speech" 
                name="pos" id="" 
                class="bg-blue-50 w-full py-3 px-4 rounded outline-blue-500">
            <textarea 
                v-model="description"
                name="description" 
                placeholder="Enter Description(In English)" 
                id="" 
                cols="30" 
                class="bg-blue-50 w-full py-3 px-4 rounded outline-blue-500" 
                rows="10"
            ></textarea>
            <textarea 
                v-model="inSentence"
                name="inSentence" 
                placeholder="Use the Word In the sentece" 
                id="" 
                cols="30" 
                class="bg-blue-50 w-full py-3 px-4 rounded outline-blue-500" 
                rows="10"
            ></textarea>
            <button class="bg-blue-500 w-full py-3 rounded text-white hover:bg-transparent hover:border-2 hover:border-blue-500 hover:text-black" type="submit">Submit</button>
        </form>
    </main>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Post',
    data() {
        return{
            words: [],
            word: '',
            pos: '',
            description: '',
            inSentence: ''
        }
    },
    methods: {
        addWord() {
            if(this.word && this.description){
                axios({
                    method: 'post',
                    url: 'http://localhost:8000/word/',
                    data: {
                        word: this.word,
                        part_of_speech: this.pos,
                        description: this.description,
                        inSentence: this.inSentence
                    },
                    auth: {
                        username: 'skye',
                        password: '1234'
                    },
                }).then((response) => {
                    let newWord = {
                        'id': response.data.id,
                        'word': this.word,
                        'part_of_speech': this.pos,
                        'description': this.description,
                        'inSentence': this.inSentence
                    }
                    this.words.push(newWord)

                    this.word = ''
                    this.pos = ''
                    this.description = ''
                    this.inSentence = ''
                }).catch((error) => {
                    console.log(error)
                })
            }
        }
    }
}
</script>