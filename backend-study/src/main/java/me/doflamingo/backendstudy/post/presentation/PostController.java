package me.doflamingo.backendstudy.post.presentation;

import javassist.NotFoundException;
import lombok.RequiredArgsConstructor;
import me.doflamingo.backendstudy.post.application.dto.PostRequestDto;
import me.doflamingo.backendstudy.post.application.dto.PostResponseDto;
import me.doflamingo.backendstudy.post.application.PostService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.net.URI;

@RestController
@RequiredArgsConstructor
@RequestMapping("/posts")
public class PostController {

  private final PostService postService;

  @PostMapping
  public ResponseEntity<?> writePost(@Valid @RequestBody PostRequestDto requestDto) {
    PostResponseDto postResponseDto = postService.writePost(requestDto);
    URI uri = URI.create("http://localhost:8080/posts/"+postResponseDto.getId());
    return ResponseEntity.created(uri).body(postResponseDto);
  }

  @GetMapping
  public ResponseEntity<?> getPostList() {
    return ResponseEntity.ok(postService.getPostList());
  }

  @GetMapping("/{id}")
  public ResponseEntity<?> getPost(@PathVariable Long id) throws NotFoundException {
    PostResponseDto postResponseDto = postService.getPostById(id)
                                        .orElseThrow(() -> new NotFoundException("post is not found"));
    return ResponseEntity.ok(postResponseDto);
  }

  @PutMapping("/{id}")
  public ResponseEntity<?> updatePost(@PathVariable Long id, @RequestBody PostRequestDto requestDto) throws NotFoundException {
    PostResponseDto postResponseDto = postService.updatePost(id, requestDto)
                                        .orElseThrow(() -> new NotFoundException("post is not found"));
    return ResponseEntity.ok(postResponseDto);
  }

  @DeleteMapping("/{id}")
  public ResponseEntity<?> deletePost(@PathVariable Long id) throws NotFoundException {
    postService.deletePost(id);
    return new ResponseEntity<>(HttpStatus.NO_CONTENT);
  }


}
