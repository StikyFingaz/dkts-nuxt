<script setup lang="ts">
const route = useRoute();

const { data: actor, refresh } = await useFetch(setApiUrl(`/actors/${route.params.nickname}`), {
  key: route.params.nickname,
  headers: { "X-User-Locale": useState("userLocale") },
});

onMounted(async () => {
  // await refresh();
});
</script>

<template lang="html">
  <div id="actorContainer">
    <ActorID>
      <template #images>
        <!-- <img :src="`/media/actors/${actor.nickname}/profile.jpg`" class="img-fluid" alt="" /> -->
        <NuxtImg
          format="webp"
          :src="`/media/actors/${actor.nickname}/profile.jpg`"
          :alt="`Profile - ${actor.nickname}`"
          class="img-fluid"
          width="1040"
          height="1290"
          sizes="300px md:640 lg:280 xl:400 xxl:400"
          :placeholder="[104, 129, 1, 15]"
        />
      </template>
    </ActorID>
    <ActorPlays />
  </div>
</template>

<style lang="css" scoped></style>
