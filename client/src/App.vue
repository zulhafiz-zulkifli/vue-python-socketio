<template>
  <h1>You did it!</h1>
</template>

<script setup>
import { io } from "socket.io-client";
import { onMounted, onBeforeUnmount } from "vue";

const socket = io("http://localhost:5000", {
  // autoConnect: true,
});

onMounted(() => {
  socket.on("connect", () => {
    console.log(socket.connected); // true
    console.log("Connected to server:", socket.id);
  });

  socket.on("disconnect", () => {
    console.log(socket.connected); // false
    console.log("Disconnected from server");
  });

  socket.io.on("reconnect", () => {
    // ...
  });

  socket.on("ping", () => {
    console.log("Ping received from server");
    // socket.emit("ping");
  });

  socket.on("publish", (data) => {
    console.log("Publish received from server:", data);
    // socket.emit("ping");
  });
});

onBeforeUnmount(() => {
  socket.close();
});
</script>

<style scoped></style>
