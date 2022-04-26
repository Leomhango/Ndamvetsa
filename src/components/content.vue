<template>
    <section class="flex flex-col w-10/12 my-10" v-for="word in words" :key="word.id">
		<h1 class="font-bold text-xl">{{ word.word }}</h1>
		<div class="ml-4">
			<p class="lowercase text-gray-500 italic text-lg">{{ word.part_of_speech }}</p>
			<p class="">{{ word.description }}</p>
			<p class="font-light text-gray-700">"{{ word.inSentence}}"</p>
		</div>
	</section>
</template>

<script>
export default {
    name: 'Content',
    props: [
        'words'
    ]
}
</script>