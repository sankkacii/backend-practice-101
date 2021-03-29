package me.doflamingo.backendstudy.post.domain;

import me.doflamingo.backendstudy.post.domain.Post;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PostRepository extends JpaRepository<Post, Long> {
}
