<script setup lang="ts">
const { data: play } = useNuxtData("playData");
const displaySize = useState("displaySize");
</script>

<template lang="html">
  <div class="container mt-3">
    <div v-if="play.actors" id="actorsCarousel" class="container-fluid">
      <Swiper
        :modules="[SwiperAutoplay]"
        slidesPerView="auto"
        :centeredSlidesBounds="true"
        :centerInsufficientSlides="true"
        :autoplay="{
          delay: 3500,
          disableOnInteraction: true,
        }"
      >
        <SwiperSlide v-for="actor in play.actors" :key="actor.nickname" class="m-2">
          <!-- <div class="col-11 col-md-6 col-lg-4 col-xl-3 card-col p-2"> -->
          <ActorCard :nickname="actor.nickname">
            <template #images>
              <img
                v-if="['xs', 'sm', 'md'].includes(displaySize)"
                :src="setThumborUrl(`/media/actors/${actor.nickname}/profile.jpg`, 'unsafe/320x0/filters:format(webp)')"
                :alt="`Photo - ${actor.name}`"
                class="card-img-top img-fluid"
                width="320"
                height="397"
                loading="lazy"
              />
              <img
                v-if="['lg', 'xl', 'xxl'].includes(displaySize)"
                :src="setThumborUrl(`/media/actors/${actor.nickname}/profile.jpg`, 'unsafe/300x0/filters:format(webp)')"
                :alt="`Photo - ${actor.name}`"
                class="card-img-top img-fluid"
                width="300"
                height="372"
                loading="lazy"
              />
              <!-- <NuxtImg
                format="webp"
                :src="`/media/actors/${actor.nickname}/profile.jpg`"
                :alt="`Photo - ${actor.name}`"
                class="card-img-top img-fluid gallery-slide"
                width="1000"
                height="1240"
                sizes="310px md:40vw lg:300px"
                loading="lazy"
              /> -->
            </template>
            <template #name>
              {{ getTranslation(actor, "name") }}
            </template>
          </ActorCard>
        </SwiperSlide>
      </Swiper>
    </div>
  </div>
</template>

<style lang="css" scoped>
.swiper-slide {
  max-width: 310px;

  @media (min-width: 768px) {
    max-width: 40vw;
  }

  @media (min-width: 992px) {
    max-width: 300px;
  }
}
</style>
