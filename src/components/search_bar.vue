<template>
    <section action="" class="mt-8 w-10/12">
        <input 
            v-model="term"
            @keypress.enter="search(term)"
            type="search" 
            placeholder="Search for a word" 
            name="" id="" 
            class="bg-blue-50 py-3 px-4 rounded-md w-full outline-blue-500"
        >
    </section>
</template>

<script>

export default {
    name: "SeachBar",

    props: [
        'search'
    ],
    data() {
        return {
            term: ''
        }
    }
}
</script>
