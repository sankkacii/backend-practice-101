package me.doflamingo.backendstudy.post.service;

import javassist.NotFoundException;
import me.doflamingo.backendstudy.post.application.PostService;
import me.doflamingo.backendstudy.post.domain.Post;
import me.doflamingo.backendstudy.post.application.dto.PostRequestDto;
import me.doflamingo.backendstudy.post.application.dto.PostResponseDto;
import me.doflamingo.backendstudy.post.domain.PostRepository;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.BDDMockito.given;

@ExtendWith(SpringExtension.class)
class PostServiceTest {

  @InjectMocks
  PostService postService;

  @Mock
  PostRepository postRepository;


  @Test
  @DisplayName("게시물 작성")
  public void writePost() {
    //given
    Long fakeId = 1L;
    PostRequestDto mockRequest = createRequest(fakeId);

    Post savedPost = CreatePost(mockRequest, fakeId);

    given(postRepository.save(any())).willReturn(savedPost);
    //when
    PostResponseDto postResponseDto = postService.writePost(mockRequest);

    //then
    assertEquals(postResponseDto.getId(), savedPost.getId());
    assertEquals(postResponseDto.getTitle(), savedPost.getTitle());
    assertEquals(postResponseDto.getContent(), savedPost.getContent());
    assertEquals(postResponseDto.getWriterId(), savedPost.getWriterId());
    assertNull(postResponseDto.getUpdatedAt());

  }

  @Test
  @DisplayName("게시물 조회 by Id")
  public void getPostById() throws Exception {
    //given
    Long fakeId = 1L;
    PostRequestDto mockRequest = createRequest(fakeId);

    Post savedPost = CreatePost(mockRequest, fakeId);

    given(postRepository.findById(fakeId)).willReturn(Optional.of(savedPost));
    //when
    PostResponseDto postResponseDto = postService.getPostById(fakeId).get();

    //then
    assertEquals(postResponseDto.getId(), fakeId);
    assertNotNull(postResponseDto.getTitle());
    assertNotNull(postResponseDto.getContent());
    assertNotNull(postResponseDto.getWriterId());

  }

  @Test
  @DisplayName("게시물 리스트 조회")
  public void getPostList() {
    //given

    List<Post> postList = new ArrayList<>();
    for(long i = 1; i<= 10; i++ ) {
      PostRequestDto mockRequest = createRequest(i);
      postList.add(CreatePost(mockRequest, i));
    }

    given(postRepository.findAll()).willReturn(postList);
    //when
    List<PostResponseDto> postResponseList = postService.getPostList();

    //then
    assertEquals(postResponseList.size(), 10);

  }

  @Test
  @DisplayName("게시물 수정")
  public void updatePost() throws NotFoundException {
    //given
    Long fakeId = 1L;
    Long newId = 2L;
    PostRequestDto mockRequest = createRequest(fakeId);
    Post savedPost = CreatePost(mockRequest, fakeId);

    PostRequestDto updateRequest = createRequest(newId);
    Post updatedPost = CreatePost(updateRequest, fakeId);


    given(postRepository.findById(1L)).willReturn(Optional.of(savedPost));
    given(postRepository.save(any())).willReturn(updatedPost);
    //when
    PostResponseDto postResponseDto = postService.updatePost(fakeId,updateRequest).orElseThrow(() -> new NotFoundException("Post is Not Found"));

    //then
    assertNotEquals(postResponseDto.getTitle(), savedPost.getTitle());
    assertEquals(postResponseDto.getId(), updatedPost.getId());
    assertEquals(postResponseDto.getTitle(), updatedPost.getTitle());
    assertEquals(postResponseDto.getContent(), updatedPost.getContent());
    assertEquals(postResponseDto.getWriterId(), updatedPost.getWriterId());

  }


  @Test
  @DisplayName("게시물 삭제")
  public void deletePost() throws Exception {
    //given
    Long fakeId = 1L;

    PostRequestDto mockRequest = createRequest(fakeId);
    Post post = CreatePost(mockRequest, fakeId);


    given(postRepository.findById(fakeId)).willReturn(Optional.of(post));
    //when
    postService.deletePost(fakeId);

    //then
    assertDoesNotThrow(() -> new NotFoundException("Post is Not Found"));

  }



  @Test
  @DisplayName("게시물 삭제 예외")
  public void deletePostWithException() {
    //given
    Long fakeId = 1L;

    PostRequestDto mockRequest = createRequest(fakeId);
    Post post = CreatePost(mockRequest, fakeId);


    given(postRepository.findById(fakeId)).willReturn(Optional.of(post));
    //when
    assertThrows(NotFoundException.class,() -> postService.deletePost(2L));

  }

  private Post CreatePost(PostRequestDto mockRequest, Long id) {
    return Post.builder()
             .id(id)
             .title(mockRequest.getTitle())
             .content(mockRequest.getContent())
             .writerId(mockRequest.getWriterId())
             .createdAt(LocalDateTime.now())
             .build();
  }
  private PostRequestDto createRequest(Long id) {
    return PostRequestDto.builder()
             .title("Test"+id)
             .content("test")
             .writerId("user")
             .build();
  }

}