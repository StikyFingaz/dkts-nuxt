<script setup lang="ts">
const { data: images } = useNuxtData("carouselImages");
const displaySize = useState("displaySize");

onMounted(() => {
  // if (error.value) {
  //   console.error("Failed to fetch play data:", error.value);
  // }
});
</script>

<template lang="html">
  <div v-show="['xs', 'sm'].includes(displaySize)" id="mobileCarousel" class="container col-11 border border-0 mt-3">
    <Swiper
      :modules="[SwiperAutoplay, SwiperEffectCoverflow, SwiperPagination, SwiperVirtual]"
      effect="coverflow"
      :virtual="{
        enabled: true,
      }"
      :autoplay="{
        delay: 3500,
        disableOnInteraction: true,
      }"
      :pagination="{
        enabled: true,
        type: 'bullets',
      }"
    >
      <SwiperSlide v-for="img in images.mobileImages" :key="`mobile-${img}`">
        <NuxtLinkLocale :to="`/events/plays/${img.split('.')[0]}`" class="col-12">
          <!-- <img
            :key="img"
            :src="setThumborUrl(`/media/main-carousel/mobile/${img}`, 'unsafe/350x0/filters:format(webp)')"
            class="img-fluid col-12 d-sm-block d-md-none"
            alt=""
            width="350"
            height="489"
            loading="lazy"
          /> -->
          <NuxtImg
            format="webp"
            :src="`/media/main-carousel/mobile/${img}`"
            :alt="`Poster: ${img}`"
            class="img-fluid col-12"
            width="10"
            height="14"
            sizes="350px"
            :placeholder="[10, 14]"
            loading="lazy"
          />
        </NuxtLinkLocale>
      </SwiperSlide>
    </Swiper>
  </div>
</template>

<style lang="css" scoped>
.swiper {
  --swiper-pagination-color: whitesmoke;
  /* --swiper-pagination-bottom: 0px; */
}
</style>
