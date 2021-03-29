package me.doflamingo.backendstudy.post.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import me.doflamingo.backendstudy.post.application.dto.PostRequestDto;
import me.doflamingo.backendstudy.post.application.dto.PostResponseDto;
import me.doflamingo.backendstudy.post.presentation.PostController;
import me.doflamingo.backendstudy.post.application.PostService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.BDDMockito.given;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;


@WebMvcTest(PostController.class)
class PostControllerTest {

  @Autowired
  MockMvc mockMvc;

  @Autowired
  ObjectMapper objectMapper;

  @MockBean
  PostService postService;

  @Test
  @DisplayName("게시글 작성")
  public void writePost() throws Exception {
    //given
    PostRequestDto mockRequest = PostRequestDto.builder()
                                      .title("Test1")
                                      .content("test")
                                      .writerId("user")
                                      .build();
    PostResponseDto mockResponse = generateResponseDto(1L);
    given(postService.writePost(any())).willReturn(mockResponse);
    //when
    mockMvc.perform(post("/posts")
      .contentType(MediaType.APPLICATION_JSON)
      .content(objectMapper.writeValueAsString(mockRequest))
    )
    //then
    .andDo(print())
    .andExpect(status().isCreated())
    .andExpect(header().exists(HttpHeaders.LOCATION))
    .andExpect(jsonPath("id").value(1L));
  }

  @Test
  @DisplayName("게시글 리스트 조회")
  public void getPosts() throws Exception {
    //given
    List<PostResponseDto> mockResponseList = new ArrayList<>();
    for(long i = 1L; i < 11L; i++){
      mockResponseList.add(generateResponseDto(i));
    }

    given(postService.getPostList()).willReturn(mockResponseList);
    //when
    mockMvc.perform(get("/posts")
                      .contentType(MediaType.APPLICATION_JSON)
    )
      //then
      .andDo(print())
      .andExpect(status().isOk());
  }

  @Test
  @DisplayName("게시글 조회")
  public void getPostById() throws Exception {
    //given

    PostResponseDto mockResponse = generateResponseDto(1L);

    given(postService.getPostById(any())).willReturn(Optional.of(mockResponse));
    //when
    mockMvc.perform(get("/posts/1")
                      .contentType(MediaType.APPLICATION_JSON)
    )
      //then
      .andDo(print())
      .andExpect(status().isOk())
      .andExpect(jsonPath(".id").value(1));
  }

  @Test
  @DisplayName("게시글 수정")
  public void updatePost() throws Exception {
    //given

    PostRequestDto mockRequest = PostRequestDto.builder()
                               .title("test2")
                               .content("test2")
                               .writerId("user")
                               .build();
    PostResponseDto mockResponse = PostResponseDto.builder()
                                     .id(1L)
                                     .title(mockRequest.getTitle())
                                     .content(mockRequest.getContent())
                                     .writerId(mockRequest.getWriterId())
                                     .createdAt(LocalDateTime.now())
                                     .updatedAt(LocalDateTime.now())
                                     .build();
    given(postService.updatePost(any(), any())).willReturn(Optional.of(mockResponse));
    //when
    mockMvc.perform(put("/posts/1")
      .contentType(MediaType.APPLICATION_JSON)
      .content(objectMapper.writeValueAsString(mockRequest))
    )
      //then
    .andDo(print())
    .andExpect(status().isOk())
    .andExpect(jsonPath(".id").value(1))
    .andExpect(jsonPath(".title").value(mockRequest.getTitle()))
    .andExpect(jsonPath(".content").value(mockRequest.getContent()));
  }

  @Test
  @DisplayName("게시글 삭제")
  public void deletePost() throws Exception {
    //given


    //given(boardService.deletePost(any())).willReturn(Optional.of(mockResponse));
    //when
    mockMvc.perform(delete("/posts/1")
                      .contentType(MediaType.APPLICATION_JSON)
    )
      //then
      .andDo(print())
      .andExpect(status().is2xxSuccessful());
  }



  private PostResponseDto generateResponseDto(Long id) {
    return PostResponseDto.builder()
             .id(id)
             .title("Test"+id)
             .content("test")
             .writerId("user")
             .createdAt(LocalDateTime.now())
             .build();
  }


}