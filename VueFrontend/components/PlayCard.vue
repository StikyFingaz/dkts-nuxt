<script setup lang="ts">
defineProps<{
  playLink?: string;
  isCurrent?: boolean;
  ticketLink?: string;
}>();

const userLocale = useState("userLocale");
</script>

<template lang="html">
  <div class="card play-card">
    <NuxtLinkLocale :to="`/events/plays/${playLink}`">
      <slot name="images"> </slot>
    </NuxtLinkLocale>
    <div class="card-body text-bg-dark d-flex justify-content-between p-0">
      <span class="card-title text-truncate m-1 ms-2 fs-5">
        <slot name="name"> </slot>
      </span>
      <a
        v-if="isCurrent && ticketLink"
        :href="`https://www.entase.bg/book?eid=${ticketLink}&lc=${userLocale}`"
        class="link-light m-1 me-2 fs-5 d-flex align-items-center"
        @click.prevent="openTicketPopup(`https://www.entase.bg/book?eid=${ticketLink}&lc=${userLocale}`)"
      >
        <Icon name="bi:ticket-perforated" />
      </a>
    </div>
  </div>
</template>

<style lang="css" scoped></style>
