<template>
   <div id="app">
      <sorted-table :values="values">
         <thead>
            <tr>
               <th scope="col" style="text-align: left; width: 10rem;">
                  <sort-link name="id">Номер</sort-link>
               </th>
               <th scope="col" style="text-align: left; width: 10rem;">
                  <sort-link name="name">Наименование</sort-link>
               </th>
               <th scope="col" style="text-align: left; width: 10rem;">
                  <sort-link name="hits">Рейтинг</sort-link>
               </th>
            </tr>
         </thead>
         <template #body="sort">
            <tbody>
               <tr v-for="value in sort.values" :key="value.id">
                  <td>{{ value.id }}</td>
                  <td>{{ value.name }}</td>
                  <td>{{ value.hits }}</td>
                  <td>
                     <button type="button" class="btn" @click="showModal(value)">
                        Подробнее!
                     </button>
                     <Modal v-show="isModalVisible" @close="closeModal" :modalData="value"/>
                  </td>
               </tr>
            </tbody>
         </template>
      </sorted-table>
   </div>
</template>

<script>
import Modal from '@/components/modal-window'

export default {
   name: "App",
   components: {
      Modal
   },
   data: function () {
      return {
         modalData: null,
         values: [
            { name: "Подрядчик 1", id: 1, hits: 4.5, about:"Подробная информация про подрядчика 1" },
            { name: "Подрядчик 2", id: 2, hits: 4, about:"Подробная информация про подрядчика 2" },
            { name: "Подрядчик 3", id: 3, hits: 3.1, about:"Подробная информация про подрядчика 3" },
            { name: "Подрядчик 4", id: 4, hits: 4.9, about:"Подробная информация про подрядчика 4" },
            { name: "Подрядчик 5", id: 5, hits: 5, about:"Подробная информация про подрядчика 5"},
            { name: "Подрядчик 6", id: 6, hits: 2.7, about:"Подробная информация про подрядчика 6" },
            { name: "Подрядчик 7", id: 7, hits: 1.9, about:"Подробная информация про подрядчика 7" }
         ],
         isModalVisible: false
      };
   },
   methods: {
      showModal(value) {
        this.modalData = this.value;
        this.isModalVisible = true;
        console.log(value);
      },
      closeModal() {
        this.isModalVisible = false;
      }
   }
};
</script>