package me.doflamingo.backendstudy.post.application.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Getter @Builder
@NoArgsConstructor @AllArgsConstructor
public class PostResponseDto {

  private Long id;

  private String title;

  private String content;

  private String writerId;

  private LocalDateTime createdAt;

  private LocalDateTime updatedAt;



}
