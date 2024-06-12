<script setup lang="ts"></script>

<template lang="html">
  <div class="card">
    <slot name="images"></slot>
    <div class="card-body">
      <h1 class="card-title display-5"><slot name="title"></slot></h1>
      <span class="card-text">
        <slot name="cardText"></slot>
      </span>
      <slot name="buttons"></slot>
    </div>
  </div>
</template>

<style lang="css" scoped></style>
