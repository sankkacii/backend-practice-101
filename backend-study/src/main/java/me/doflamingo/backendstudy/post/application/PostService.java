package me.doflamingo.backendstudy.post.application;

import javassist.NotFoundException;
import lombok.RequiredArgsConstructor;
import me.doflamingo.backendstudy.post.domain.Post;
import me.doflamingo.backendstudy.post.application.dto.PostRequestDto;
import me.doflamingo.backendstudy.post.application.dto.PostResponseDto;
import me.doflamingo.backendstudy.post.domain.PostRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;


import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.function.Supplier;

@Service
@Transactional
@RequiredArgsConstructor
public class PostService {

  private final PostRepository postRepository;

  public PostResponseDto writePost(PostRequestDto requestDto) {
    Post post = Post.builder()
                  .title(requestDto.getTitle())
                  .content(requestDto.getContent())
                  .writerId(requestDto.getWriterId())
                  .createdAt(LocalDateTime.now())
                  .build();
    Post savedPost = postRepository.save(post);

    return changePostToPostResponseDto(savedPost);
  }

  @Transactional(readOnly = true)
  public List<PostResponseDto> getPostList() {
    List<Post> postList = postRepository.findAll();
    List<PostResponseDto> postResponseList = new ArrayList<>();
    for (Post post : postList) {
      postResponseList.add(changePostToPostResponseDto(post));
    }
    return postResponseList;
  }

  @Transactional(readOnly = true)
  public Optional<PostResponseDto> getPostById(Long id) throws NotFoundException {
    Post findPost = postRepository.findById(id).orElseThrow(Post_is_not_found());
    return Optional.of(changePostToPostResponseDto(findPost));
  }

  public Optional<PostResponseDto> updatePost(Long id, PostRequestDto requestDto) throws NotFoundException {
    Post findPost = postRepository.findById(id).orElseThrow(Post_is_not_found());

    Post updatePost = Post.builder()
                        .id(findPost.getId())
                        .title(requestDto.getTitle())
                        .content(requestDto.getContent())
                        .writerId(requestDto.getWriterId())
                        .createdAt(findPost.getCreatedAt())
                        .updatedAt(LocalDateTime.now())
                        .build();
    Post updatedPost = postRepository.save(updatePost);
    return Optional.of(changePostToPostResponseDto(updatedPost));
  }

  public void deletePost(Long id) throws NotFoundException {
    Post post = postRepository.findById(id).orElseThrow(Post_is_not_found());
    postRepository.delete(post);

  }

  private Supplier<NotFoundException> Post_is_not_found() {
    return () -> new NotFoundException("Post is Not Found");
  }

  private PostResponseDto changePostToPostResponseDto(Post post) {
    return PostResponseDto.builder()
             .id(post.getId())
             .title(post.getTitle())
             .content(post.getContent())
             .writerId(post.getWriterId())
             .createdAt(post.getCreatedAt())
             .updatedAt(post.getUpdatedAt())
             .build();
  }
}
