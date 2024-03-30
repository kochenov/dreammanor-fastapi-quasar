import { api } from "boot/axios";

/*
 * перехватчик ответов
 */
api.interceptors.response.use(
  (response) => response,
  (error) => {
    return Promise.reject(error);
  }
);
/**
 *
 */
export const parser = {
  /**
   * Get Items
   * @returns
   */
  async getItemsRepository(url, filters) {
    try {
      let res = await api.get(url, {params: filters});
      console.log(res.data);
      return res.data;
    } catch (error) {
      console.log(error.response);
      return error.response;
    }
  },

};
